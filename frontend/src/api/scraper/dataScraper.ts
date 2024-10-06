import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ScrapingService {

  constructor(private http: HttpClient) {}

  scrapePage(url: string): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/api/scrape', { url });
  }
}
