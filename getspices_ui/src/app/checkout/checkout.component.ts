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
  billing_details: any;

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
    data["user_id"] = 1;
    this.api.placeOrder(data).subscribe((data) => { 
      this.billing_details = data; 
      const billing_id = this.billing_details['id']
      this.router.navigate(['payment'], { queryParams: {bill_id: billing_id} });
    });
  }

}
