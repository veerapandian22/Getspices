import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-shop-details',
  templateUrl: './shop-details.component.html',
  styleUrls: ['./shop-details.component.css']
})
export class ShopDetailsComponent {

  single_item_id: any;
  single_item_details: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.single_item_id = params });
  } 

  ngOnInit() {
    this.getSingleItem();
  }

  getSingleItem() {
    this.api.getSingleItem(this.single_item_id).subscribe((data: any) => { this.single_item_details = data });
  }

  redirectToCart(product_id: number, product_item_id: number) {
    // FIXME: current_user_id
    const current_user_id = 1;
    this.addToCart(current_user_id, product_id, product_item_id);
    this.router.navigate(['cart'], { queryParams: { user_id: current_user_id }});
  }

  addToCart(user_id: number, product_id: number, product_item_id: number) {
    const data = new FormData();
    data.append('user_id', String(user_id));
    data.append('product_id', String(product_id));
    data.append('product_item_id', String(product_item_id));

    this.api.addToCart(data).subscribe((res: any) => {});
  }


}
