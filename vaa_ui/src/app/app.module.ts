import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { ContactComponent } from './contact/contact.component';
import { AboutComponent } from './about/about.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CartComponent } from './cart/cart.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { NewsComponent } from './news/news.component';
import { ShopComponent } from './shop/shop.component';
import { SinglenewsComponent } from './singlenews/singlenews.component';
import { SingleproductComponent } from './singleproduct/singleproduct.component';
import { Notfound404Component } from './notfound404/notfound404.component';
import { HttpClientModule } from '@angular/common/http'
import { FormsModule } from '@angular/forms';
import { UserOrderDetailsComponent } from './user-order-details/user-order-details.component'

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    ContactComponent,
    AboutComponent,
    DashboardComponent,
    CartComponent,
    CheckoutComponent,
    NewsComponent,
    ShopComponent,
    SinglenewsComponent,
    SingleproductComponent,
    Notfound404Component,
    UserOrderDetailsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
