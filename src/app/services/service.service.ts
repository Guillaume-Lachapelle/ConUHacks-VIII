import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root',
})
export class ServiceService {
  constructor(private _http: HttpClient) {}
  getdata() {
    return this._http.get('http://127.0.0.1:5000/api/data');
  }
}
