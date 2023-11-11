import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-delivery-info',
  templateUrl: './delivery-info.component.html',
  styleUrls: ['./delivery-info.component.css']
})
export class DeliveryInfoComponent {

  deliveryInfo: any;

  constructor(
    private api: UserService,
    private toastr: ToastrService
  ) {}

  ngOnInit() {
    this.getDeliveryInfo();
    this.showSuccess();
  }

  getDeliveryInfo() {
    this.api.deliveryInfo().subscribe((res)=>{this.deliveryInfo = res, console.warn(this.deliveryInfo)});
  }

  showSuccess() {
    this.toastr.success('Order placed successfully!');
  }

}
