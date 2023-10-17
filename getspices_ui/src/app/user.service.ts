import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  getProducts() {
    return this.http.get<any>('http://127.0.0.1:8000/api/product');
  }

}
