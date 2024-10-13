import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Article {
  title: string;
  date: string;
  summary: string;
}

@Component({
  selector: 'app-article-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './article-list.component.html',
  styleUrl: './article-list.component.css'
})

export class ArticleListComponent {//PLACEHOLER  DATA
  articles: Article[] = [
    {
      title: "Breakthrough in Renewable Energy Technology",
      date: "2024-10-13",
      summary: "Scientists have developed a new method to harness solar energy that could significantly reduce costs and improve efficiency."
    },
    {
      title: "Global Economic Outlook for 2025",
      date: "2024-10-12",
      summary: "Experts predict a slow recovery in global markets as inflation continues to impact various sectors."
    },
    {
      title: "New Health Guidelines for Nutrition",
      date: "2024-10-11",
      summary: "The World Health Organization has released updated dietary recommendations aimed at promoting healthier eating habits worldwide."
    },
    {
      title: "Advancements in Artificial Intelligence",
      date: "2024-10-10",
      summary: "Researchers have made significant strides in AI, developing systems that can learn and adapt faster than ever before."
    },
    {
      title: "Climate Change and Its Impact on Wildlife",
      date: "2024-10-09",
      summary: "A new study reveals alarming trends in wildlife populations as climate change continues to disrupt ecosystems."
    }
  ];
}
