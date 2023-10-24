import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';
import {NgForm} from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-contact-us',
  templateUrl: './contact-us.component.html',
  styleUrls: ['./contact-us.component.css']
})
export class ContactUsComponent {
  
  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute,
    private toastr: ToastrService
  ) {}

  onSubmit(data: any, contactUs : NgForm) {
    this.api.contactUS(data).subscribe((res) => { 
      contactUs.reset();
      this.showSuccessMsg();
    });
  }

  showSuccessMsg() {
    this.toastr.success('We appreciate you contacting us.', 'Thank you for getting in touch!');
  }


}
