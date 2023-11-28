import { Injectable, NgModule, Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';
import { JwtHelperService } from '@auth0/angular-jwt';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  session_user_id: number | undefined;
  token: any;
  helper_service: any;
  
  constructor(
    private http: HttpClient,
    private api: UserService,
    private cookieService: CookieService
  ) {}

  ngOnInit() {
    this.login();
  }

  login() {
    var data = {"username": "veera", "password": "12345A!a"}
    this.api.userLogin(data).subscribe((token: any) => { this.token = token,
      this.helper_service = new JwtHelperService();
      this.cookieService.set('authToken', token.access);
      let access_token = this.cookieService.get('authToken');
      var token_decoded = this.helper_service.decodeToken(access_token);
      console.warn(token.access);
      console.log(token_decoded);
    });
  }



}
