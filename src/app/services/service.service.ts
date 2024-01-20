import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ServiceService {
  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {}

  generate_map(): Observable<SafeHtml> {
    return this.http
      .get('http://localhost:5000/generate_map', { responseType: 'text' })
      .pipe(
        map((data) => {
          return this.sanitizer.bypassSecurityTrustHtml(data);
        })
      );
  }
  generate_map2(): Observable<SafeHtml> {
    return this.http
      .get('http://localhost:5000/generate_map2', { responseType: 'text' })
      .pipe(
        map((data) => {
          return this.sanitizer.bypassSecurityTrustHtml(data);
        })
      );
  }
}
