import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { UploadService } from './services/upload.service';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { AuthService } from './services/auth.service';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes), 
    provideAnimationsAsync(),
    provideHttpClient(
      // withFetch(),
    ),
    {
      provide: UploadService,
    },
    {
      provide: AuthService,
    }
  ]
};
