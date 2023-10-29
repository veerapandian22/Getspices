import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';
import { ToastrService } from 'ngx-toastr';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent {

  constructor(
    private api: UserService,
    private http: HttpClient,
    private toastr: ToastrService
  ) { }

  onSubmit(data: any, userSubscribe : NgForm) {
    this.api.subscribe(data).subscribe((res) => { userSubscribe.reset(); this.showSuccess(); });
  }

  showSuccess() {
    this.toastr.success('Thank you for subscribing!');
  }

}
