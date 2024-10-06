import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  url: string = '';
  scrapedData: any = null;
  errorMessage: string = '';
  isLoading: boolean = false;

  scrapePage() {
    this.isLoading = true;
    setTimeout(() => {
      this.scrapedData = {
        title: 'Mocked Title',
        description: 'Mocked description for the scraped page.'
      };
      this.isLoading = false;
    }, 1000);
  }
}
