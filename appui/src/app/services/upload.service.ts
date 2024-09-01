import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  private urls = {
    upload: "http://localhost:9000/v1/u/",
    get_all_uploads: "http://localhost:9000/v1/u/",
    download: "http://localhost:9000/v1/d/"
  }

  constructor(
    private httpclient: HttpClient
  ) { }

  fileName: string = "";

  upload(file: any) {
    this.fileName = file.name;

    const formData = new FormData();
    formData.append("file", file);


    this.httpclient.post(this.urls.upload, formData).subscribe(e => {
      console.log(e)
    })

  }
}
