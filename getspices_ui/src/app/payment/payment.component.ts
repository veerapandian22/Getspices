import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent {

  bill_id: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.bill_id = params });
  }

  onSubmit(data: any) {
    // FIXME: user id
    const query: any = {};
    query['user_id'] = 1;
    query['bill_id'] = this.bill_id['bill_id'];
    query['payment_verified_admin_name'] = 'system';  // default value for Initial payment
    if (data['pay'] == "UPI")
      query['is_upi'] = 1;
    else if (data['pay'] == "COD")
      query['is_cash_on_delivery'] = 1;

    this.api.payment(query).subscribe({
      next: (response) => {
        this.router.navigate(['delivery_info'], { queryParams: {user_id: 1}});
      },
      error: (error) => {
          console.warn(error.status);
      },
    });
  }

}
