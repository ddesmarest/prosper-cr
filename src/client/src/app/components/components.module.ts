import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { MainFrameComponent } from './main-frame/main-frame.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { EditUserComponent } from './edit-user/edit-user.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { RouterModule, Routes } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';

@NgModule({
  imports: [
    CommonModule, FormsModule, RouterModule
  ],
  declarations: [LoginComponent, MainFrameComponent, NavBarComponent, EditUserComponent, PageNotFoundComponent, WelcomeComponent],
  exports: [LoginComponent, MainFrameComponent, EditUserComponent, PageNotFoundComponent, WelcomeComponent]
})
export class ComponentsModule { }
