import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  getProductApiCall() {
    return this.http.get<any>('http://127.0.0.1:8000/api/product/');
  }

  getProductsFromCart() {
    return this.http.get<any>('http://127.0.0.1:8000/api/cart/');
  }

  removeProductFromCart(data: any) {
    return this.http.delete<any>('http://127.0.0.1:8000/api/cart/', data);
  }

  getProductLists(data: any) {
    console.warn(data)
    return this.http.get<any>('http://127.0.0.1:8000/api/product_list/'+data['product_id']+'/');
  }

  addProductListToCart(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/cart/', data);
  }

  addPlaceOderDetails(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/checkout/', data);
  }

}
