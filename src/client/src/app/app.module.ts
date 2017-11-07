import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServicesModule } from './services/services.module';
import { ComponentsModule } from './components/components.module'
import { appRoutes } from './app-routing-module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule, ServicesModule, ComponentsModule,
    RouterModule.forRoot(
      appRoutes,
      { /*enableTracing: true*/ } // <-- debugging purposes only
    ),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
