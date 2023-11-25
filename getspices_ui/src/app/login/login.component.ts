import { Injectable, NgModule, Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../user.service';
import { JwtHelperService } from '@auth0/angular-jwt';
// import { Cookie } from 'ng2-cookies/ng2-cookies';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  
  loginUser: any = {
    email: '',
    password: '',
  };

  session_user_id: number | undefined;
  access_token: any;
  helper_service: any;
  
  constructor(
    private http: HttpClient,
    private api: UserService,
  ) {}

  ngOnInit() {
    this.login();
  }

  // login() {
  //   var data = {"username": "veera", "password": "12345A!a"}
  //   this.api.userLogin(data).subscribe( {
  //     next: () => {
  //       console.warn(token)
  //       alert('login successful');
  //     },
  //     error: (error) => {
  //       alert('login failed');
  //     },
  //   });
  // }
  login() {
    var data = {"username": "veera", "password": "12345A!a"}
    this.api.userLogin(data).subscribe((token: any) => { this.access_token = token,
      this.helper_service = new JwtHelperService();
      var decoded = this.helper_service.decodeToken('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwNDEwMDcyLCJpYXQiOjE3MDA0MDk3NzIsImp0aSI6ImI5MTNlYmI3ZDczMjRjNjI4NGQ0NTFmNjM3ZjUyNDIwIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ2ZWVyYSJ9.qu0v-8jPcIVZiHYJvaDyvPDHJRt8E-x5o7ynRyRxs_8');
      console.warn(token.access);
      console.log(decoded)
      // Cookie.set('jwtToken', 'tokenValue');
      // let tokena = Cookie.get('jwtToken');
      // console.warn(tokena)

    });
  }



}
