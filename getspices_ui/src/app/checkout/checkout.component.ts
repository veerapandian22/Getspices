import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent {

  user_id: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.user_id = params });
  }

  ngOnInit() {}

  onPlaceOrder(data: any) {
    // FIXME: user id
    console.warn(data)
    data["user_id"] = 1;
    this.api.placeOrder(data).subscribe((res) => { console.warn('placeOrder', res) })
    this.redirectToDeliveryInfo();
  }

  redirectToDeliveryInfo() {
    // FIXME: user id
    this.router.navigate(['delivery_info'], { queryParams: {user_id: 1}});
  }

}
