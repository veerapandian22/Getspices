import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-user-order-details',
  templateUrl: './user-order-details.component.html',
  styleUrls: ['./user-order-details.component.css']
})
export class UserOrderDetailsComponent {

  orderDetails: any;
  login_user_id: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.login_user_id = params });
  }


  ngOnInit() {
    this.fetchOrderDetails()
  }


  fetchOrderDetails() {
    // FIXME: login_user_id
    const login_user_id = 1
    this.api.getOrderDetails(login_user_id).subscribe((data) => this.orderDetails = data);
  }


}
