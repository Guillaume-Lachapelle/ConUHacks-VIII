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

  constructor(private _apiservice: ServiceService) {}

  ngAfterViewInit() {
    this.getData();
    this.getData2();
  }

  async getData() {
    this._apiservice
      .generate_map()
      .pipe()
      .subscribe((mapHtml) => {
        this.finishedFetching = true;
      });
  }
  async getData2() {
    this._apiservice
      .generate_map2()
      .pipe()
      .subscribe((mapHtml) => {
        console.log('ym');
        console.log(mapHtml);
        this.finishedFetching2 = true;
      });
  }
}
