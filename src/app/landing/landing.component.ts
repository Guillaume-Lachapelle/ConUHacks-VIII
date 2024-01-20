import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ServiceService } from '../services/service.service';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss'],
})
export class LandingComponent {
  newdata: any;

  constructor(private _apiservice: ServiceService) {}

  ngOnInit() {
    this.getData();
  }

  getData() {
    this._apiservice.getdata().subscribe((res) => {
      this.newdata = res;
    });
  }
}
