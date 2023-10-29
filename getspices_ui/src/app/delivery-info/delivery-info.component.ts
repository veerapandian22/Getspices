import { Component } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-delivery-info',
  templateUrl: './delivery-info.component.html',
  styleUrls: ['./delivery-info.component.css']
})
export class DeliveryInfoComponent {

  constructor(
    private toastr: ToastrService
  ) {}

  ngOnInit() {
    this.showSuccess();
  }

  showSuccess() {
    this.toastr.success('Order placed successfully!');
  }

}
