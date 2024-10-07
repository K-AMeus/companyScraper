import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ScrapingService } from '../../api/scraper/dataScraper';

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

  constructor(private scrapingService: ScrapingService) {} 

  scrapePage() {
    this.isLoading = true;
    setTimeout(() => {
      this.scrapingService.scrapePage(this.url).subscribe({
          next: (data) => {
            this.scrapedData = {
              title: data.title,
              description: data.description
            }
          }
      });
      this.isLoading = false;
    },1000);

  }
}

