import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServicesModule } from './services/services.module';
import { ComponentsModule } from './components/components.module'
import { appRoutes } from './app-routing-module';
import { AppComponent } from './app.component';
import { WorkspaceModule } from './workspace/workspace.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule, ServicesModule, ComponentsModule, WorkspaceModule,
    RouterModule.forRoot(
      appRoutes,
      { /*enableTracing: true*/ } // <-- debugging purposes only
    ),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
