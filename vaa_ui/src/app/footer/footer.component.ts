import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent {

  constructor(private http: HttpClient) { }

  onSubmit(data: any) {
    this.http.post('http://127.0.0.1:8000/api/subscribe/', data).subscribe((result)=>{
      console.warn('result', result)
    })
    console.warn(data)
  }

}
