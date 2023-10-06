import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent {

  login_user_id: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.login_user_id = params });
  }

  ngOnInit() {}

  onPlaceOrder(data: any) {
    // FIXME: user id
    console.warn(data)
    data["user"] = 1;
    this.api.addPlaceOderDetails(data).subscribe((result) => {
      console.warn('placeOrder', result)
    })
    this.redirectToOrderDetails();
  }

  redirectToOrderDetails() {
    // FIXME: user id
    this.router.navigate(['user_order_details'], { queryParams: {login_user_id: 1}});
  }

}
