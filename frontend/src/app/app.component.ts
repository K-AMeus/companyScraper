import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule, HttpClient } from '@angular/common/http'; // Import HttpClientModule

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule], // Include HttpClientModule here
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  apiResponse: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    // Call the Flask API on initialization
    this.http.get('http://127.0.0.1:5000/api/test', { responseType: 'text' })
      .subscribe((response: string) => {
        this.apiResponse = response;
      });
  }
}
