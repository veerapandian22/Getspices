import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent} from "./about/about.component";
import { DashboardComponent } from './dashboard/dashboard.component';
import { ContactComponent } from './contact/contact.component';
import { CartComponent } from './cart/cart.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { NewsComponent } from './news/news.component';
import { ShopComponent } from './shop/shop.component';
import { SinglenewsComponent } from './singlenews/singlenews.component';
import { SingleproductComponent } from './singleproduct/singleproduct.component';
import { Notfound404Component } from './notfound404/notfound404.component';
import { UserOrderDetailsComponent } from './user-order-details/user-order-details.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'cart', component: CartComponent },
  { path: 'checkout', component: CheckoutComponent },
  { path: 'news', component: NewsComponent },
  { path: 'shop', component: ShopComponent },
  { path: 'single_news', component: SinglenewsComponent },
  { path: 'single_product', component: SingleproductComponent },
  { path: 'user_order_details', component: UserOrderDetailsComponent },
  { path: 'not_found_404', component: Notfound404Component }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
