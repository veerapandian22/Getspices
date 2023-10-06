import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-singleproduct',
  templateUrl: './singleproduct.component.html',
  styleUrls: ['./singleproduct.component.css']
})
export class SingleproductComponent {

  single_product_id: any
  single_product_details: any

  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {
    this.activeRoute.queryParams.subscribe((params: any) => { this.single_product_id = params });
  } 

  ngOnInit() {
    this.fetchSingleProduct();
  }

  fetchSingleProduct() {
    this.api.getSingleProduct(this.single_product_id).subscribe((data)=>this.single_product_details = data);
  }

  // FIXME: login_user_id
  redirectToCart(id: any, product: any, name: any, image_path: any, price: any) {
    this.addToCart(id, product, name, image_path, price);
    this.router.navigate(['cart'], { queryParams: { login_user_id: 1 }});
  }

  addToCart(id: any, product: any, name: any, image_path: any, price: any) {
    // FIXME: user_id, quantity, total
    const data = new FormData();
    data.append('user', "1");
    data.append('product', product);
    data.append('product_list', id);
    data.append('product_name', name);
    data.append('product_path', image_path);
    data.append('price', price);
    data.append('quantity', "2");
    data.append('total', "0");

    this.api.addProductListToCart(data).subscribe((res) => { 
      console.warn(res) 
    });
  }

}
