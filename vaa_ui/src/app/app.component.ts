import { Component } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'vaa_ui';
  
  constructor(private api: UserService) {}

  // ngOnInit() {
	// this.api.apiCall().subscribe(data=>{
	// 	console.warn("get api data", data);
	// })
  // }

}
