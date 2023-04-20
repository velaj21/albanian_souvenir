import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-background',
  templateUrl: './background.component.html',
  styleUrls: ['./background.component.scss']
})
export class BackgroundComponent implements OnInit {
  public index: number = 0;
  public imageUrl: string = 'https://www.w3schools.com/howto/img_nature.jpg';

  ngOnInit() {
    setInterval(() => {
      let urls = ['https://upload.wikimedia.org/wikipedia/commons/1/1e/20220121%E2%80%94Sana_%EC%82%AC%EB%82%98_Campaign_Film%2C_Pearlygates_x_Twice_2022.jpg', 'https://upload.wikimedia.org/wikipedia/commons/5/55/220701_Nayeon%28%EB%82%98%EC%97%B0%29_of_Twice_MusicBank_Fancam.jpg'];
      this.imageUrl = urls[(this.index++) % 2];
    }, 1500);
  }
}
