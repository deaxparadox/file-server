import { HttpClient, HttpClientModule, HttpEventType } from '@angular/common/http';
import { Component, Input } from '@angular/core';
import { MatButtonModule, MatMiniFabButton } from "@angular/material/button";
import { MatProgressBarModule } from "@angular/material/progress-bar";

import { MatIcon } from "@angular/material/icon"
import { UploadService } from '../../services/upload.service';
import { finalize, Subscription } from 'rxjs';
import { NgIf } from '@angular/common';


@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [
    MatButtonModule,
    MatIcon,
    MatProgressBarModule,
    NgIf
  ],
  templateUrl: './upload.component.html',
  styleUrl: './upload.component.scss',
})
export class UploadComponent {

  @Input() requiredFileType: string | null = null;

  fileName = "";
  uploadProgress: number | null = null;
  uploadSub: Subscription | null = null;

  constructor(
    private uploadService: UploadService,
    private http: HttpClient
  ) {}

  onFilesSelected(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      this.fileName = file.name;

      // creating form
      const formData = new FormData();
      formData.append("file", file);


      // uploading
      const upload$ = this.http.post("http://localhost:9000/v1/u/", formData, {
        reportProgress: true,
        observe: "events"
      }).pipe(finalize(() => this.reset()));

      this.uploadSub = upload$.subscribe(event => {
        // console.log(event.type);

        if (event.type == HttpEventType.UploadProgress) {
          this.uploadProgress = Math.round(100 * (event.loaded / event.total!));
          // console.log(this.uploadProgress)
        }
      });

    }

  }


  cancelUpload() {
    this.uploadSub?.unsubscribe();
    this.reset();
  }


  reset() {
    this.uploadProgress = null;
    this.uploadSub = null;
  }

}
