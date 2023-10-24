import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent {

  isSuccess = false;
  current_user_id: any;
  items_in_cart: any

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { 
      this.current_user_id = params;
    });
  }

  ngOnInit() {
    this.cartDetails();
    this.isSuccess = true;
  }

  cartDetails() {
    // FIXME: user_id
    const user_id = 1;
    this.api.getCartDetails(user_id).subscribe((res: any) => { this.items_in_cart = res});
  }

  removeItemFromCart(id: number) {
    const data = {
      headers: new HttpHeaders({'Content-Type': 'application/json'}),
      body: { id: id },
    };
    this.api.removeItemFromCart(data).subscribe((res: any) => { this.cartDetails(); });
  }

  redirectToCheckout() {
    // FIXME: user_id
    const user_id = 1;
    this.router.navigate(['checkout'], { queryParams: {user_id: user_id}});
  }


}
