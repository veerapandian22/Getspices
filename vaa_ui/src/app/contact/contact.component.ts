import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {

  constructor(private http: HttpClient) { }

  onSubmit(data: any) {
    this.http.post('http://127.0.0.1:8000/api/contact_us/', data).subscribe((result)=>{
      console.warn('result', result)
    })
    console.warn(data)
  }

}
