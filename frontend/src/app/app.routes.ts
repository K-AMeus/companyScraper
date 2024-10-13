import { Routes } from '@angular/router';
import { HomeComponent } from '../../src/components/home/home.component';
import { AboutComponent } from '../../src/components/about/about.component';
import { ArticleListComponent } from '../components/article-list/article-list.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'article-list', component: ArticleListComponent},
  { path: '**', redirectTo: '' }
];