import { Routes } from '@angular/router';
import { HomeComponent } from '../../src/components/home/home.component';
import { AboutComponent } from '../../src/components/about/about.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: '**', redirectTo: '' }
];