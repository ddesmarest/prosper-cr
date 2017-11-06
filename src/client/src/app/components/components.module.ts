import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { MainFrameComponent } from './main-frame/main-frame.component';

@NgModule({
  imports: [
    CommonModule, FormsModule
  ],
  declarations: [LoginComponent, MainFrameComponent],
  exports: [LoginComponent, MainFrameComponent]
})
export class ComponentsModule { }
