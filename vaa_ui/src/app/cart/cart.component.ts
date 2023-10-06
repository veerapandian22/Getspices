import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-card',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent {

  products: any;
  login_user_id: any

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.login_user_id = params });
   }


  ngOnInit() {
    this.fetchcarts();
    console.warn(this.login_user_id);
  }


  fetchcarts() {
    this.api.getProductsFromCart().subscribe((data) => this.products = data);
  }

  
  removeProduct(id: number){
    const data = {
      headers: new HttpHeaders({'Content-Type': 'application/json'}),
      body: { id: id },
    };
    this.api.removeProductFromCart(data).subscribe((res) => { this.fetchcarts(); });
  }

  redirectToCheckout() {
    this.router.navigate(['checkout'], { queryParams: {login_user_id: this.login_user_id}});
  }


}
