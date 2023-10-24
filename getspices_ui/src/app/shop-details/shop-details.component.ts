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


}
