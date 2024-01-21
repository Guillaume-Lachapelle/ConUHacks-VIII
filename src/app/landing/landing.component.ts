import { Component } from '@angular/core';
import { ServiceService } from '../services/service.service';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss'],
})
export class LandingComponent {
  finishedFetching = false;
  finishedFetching2 = false;
  finishedFetching3 = false;
  lightTheme = true;
  numbers1 = [] as any;
  numbers2 = [] as any;
  numbers3 = [] as any;

  constructor(private _apiservice: ServiceService) {}

  ngAfterViewInit() {
    this.getData();
    this.getData2();
    this.getData3();
  }

  async getData() {
    this._apiservice
      .generate_map()
      .pipe()
      .subscribe((mapHtml) => {
        console.log(mapHtml);
        let numbers = mapHtml.toString().split(',');
        this.numbers1 = numbers;
        this.finishedFetching = true;
      });
  }
  async getData2() {
    this._apiservice
      .generate_map2()
      .pipe()
      .subscribe((mapHtml) => {
        console.log(mapHtml);
        let numbers = mapHtml.toString().split(',');
        this.numbers2 = numbers;
        this.finishedFetching2 = true;
      });
  }
  async getData3() {
    this._apiservice
      .generate_map3()
      .pipe()
      .subscribe((mapHtml) => {
        console.log(mapHtml);
        let numbers = mapHtml.toString().split(',');
        this.numbers3 = numbers;
        this.finishedFetching3 = true;
      });
  }

  lightThemeToggle() {
    this.lightTheme = !this.lightTheme;
  }
}
