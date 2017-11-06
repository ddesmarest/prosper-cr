import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { AuthentificationService } from './authentification.service';

@NgModule({
  imports: [
    CommonModule, HttpModule
  ],
  declarations: [],
  providers: [AuthentificationService]
})
export class ServicesModule { }
