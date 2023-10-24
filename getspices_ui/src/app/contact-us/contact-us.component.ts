import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';
import { ActivatedRoute, Router } from '@angular/router';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-contact-us',
  templateUrl: './contact-us.component.html',
  styleUrls: ['./contact-us.component.css']
})
export class ContactUsComponent {

  isSuccess = false;
  
  constructor(
    private api: UserService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {}

  onSubmit(data: any, contactUs : NgForm) {
    this.api.contactUS(data).subscribe((res) => { 
      contactUs.reset();
      this.showSuccessMsg();
    });
  }

  showSuccessMsg() {
    this.isSuccess = false;
    setTimeout(() => { this.isSuccess = true; }, 4000);
  }


}
