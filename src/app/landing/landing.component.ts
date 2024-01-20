import { Component } from '@angular/core';
import { ServiceService } from '../services/service.service';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss'],
})
export class LandingComponent {
  finishedFetching = false;

  constructor(private _apiservice: ServiceService) {}

  ngAfterViewInit() {
    this.getData();
  }

  async getData() {
    this._apiservice
      .generate_map()
      .pipe()
      .subscribe((mapHtml) => {
        this.finishedFetching = true;
      });
  }
}
