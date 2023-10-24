import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent {

  product_id: any;
  product_items: any;

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.product_id = params });
  }

  ngOnInit() {
    this.getProductItems();
  }

  getProductItems() {
    this.api.getProductItems(this.product_id).subscribe((data: any) => {this.product_items = data});
  }

  redirectToSingleItem(single_item_id: number) {
    this.router.navigate(['shop_details'], { queryParams: { single_item_id: single_item_id }});
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
