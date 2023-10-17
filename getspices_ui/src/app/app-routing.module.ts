import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ShopComponent } from './shop/shop.component';
import { BlogComponent } from './blog/blog.component';
import { CartComponent } from './cart/cart.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { ContactUsComponent } from './contact-us/contact-us.component';
import { DeliveryInfoComponent } from './delivery-info/delivery-info.component';
import { SitemapComponent } from './sitemap/sitemap.component';
import { InnovationComponent } from './innovation/innovation.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'shop', component: ShopComponent },
  { path: 'blog', component: BlogComponent },
  { path: 'cart', component: CartComponent },
  { path: 'checkout', component: CheckoutComponent },
  { path: 'about_us', component: AboutUsComponent },
  { path: 'contact_us', component: ContactUsComponent },
  { path: 'delivery_info', component: DeliveryInfoComponent },
  { path: 'sitemap', component: SitemapComponent },
  { path: 'innovation', component: InnovationComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
