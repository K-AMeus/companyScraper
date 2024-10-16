import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ScrapingService } from '../../api/scraper/dataScraper';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  companyName: string = '';
  timeRange: string = '6m'; //default
  searchResults: any = null;
  report: any = null; 
  errorMessage: string = '';
  isLoading: boolean = false;

  constructor(private scrapingService: ScrapingService) {}

  searchCompany() {
    if (!this.companyName.trim()) {
      this.errorMessage = 'Please enter a company name.';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';
    this.searchResults = null;

    this.scrapingService.searchCompany(this.companyName, this.timeRange).subscribe({
      next: (data) => {
        this.searchResults = data.items || [];
        this.isLoading = false;
      },
      error: (error) => {
        this.errorMessage = 'An error occurred while searching.';
        console.error(error);
        this.isLoading = false;
      },
    });
  }
}
