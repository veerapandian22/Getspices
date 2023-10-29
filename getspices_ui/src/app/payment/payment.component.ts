import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent {

  constructor(
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {}

  onSubmit(data: any) {
    // FIXME: user id
    this.router.navigate(['delivery_info'], { queryParams: {user_id: 1}});
  }

}
