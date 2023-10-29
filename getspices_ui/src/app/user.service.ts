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

  getProductItems(data: any) {
    return this.http.get<any>('http://127.0.0.1:8000/api/product_item/' + data['product_id']);
  }

  getSingleItem(data: any) {
    return this.http.get<any>('http://127.0.0.1:8000/api/single_item_details/' + data['single_item_id']);
  }

  addToCart(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/cart', data);
  }

  getCartDetails(user_id: number) {
    return this.http.get<any>('http://127.0.0.1:8000/api/cart/' + user_id);
  }

  removeItemFromCart(data: any) {
    return this.http.delete<any>('http://127.0.0.1:8000/api/cart', data);
  }

  placeOrder(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/billing_address', data);
  }

  contactUS(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/contact', data);
  }

  subscribe(data: any) {
    return this.http.post<any>('http://127.0.0.1:8000/api/subscribe', data);
  }

}
