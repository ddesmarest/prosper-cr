import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { WelcomeComponent } from './welcome.component';
import { ComponentsModule } from '../components.module';
import { AuthentificationService } from '../../services/authentification.service';
import { FakeAuthentificationService } from '../../services/testing/fake-authentification.service';


let comp: WelcomeComponent;
let fixture: ComponentFixture<WelcomeComponent>;
let de: DebugElement;
let el: HTMLElement;

function compileAndCreate() {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ComponentsModule],
      providers: [
        { provide: AuthentificationService, useClass: FakeAuthentificationService }

      ]
    }).compileComponents().then(() => {
      fixture = TestBed.createComponent(WelcomeComponent);
      comp = fixture.componentInstance;
    });
  }));
}
describe('WelcomeComponent (deep)', () => {
  compileAndCreate();

  it('should NOT have user before ngOnInit', () => {
    expect(comp.user).toBeNull('should not have user before ngOnInit');
  });

  /*it('should NOT have user immediately after ngOnInit', () => {
    fixture.detectChanges(); // runs initial lifecycle hooks

    expect(comp.user).toBeUndefined
      'should not have user until service promise resolves');
  });*/

  describe('after get welcome', () => {

    // Trigger component so it gets heroes and binds to them
    beforeEach(async(() => {
      fixture.detectChanges(); // runs ngOnInit -> getHeroes
      fixture.whenStable() // No need for the `lastPromise` hack!
        .then(() => fixture.detectChanges()); // bind to heroes
    }));

    it('should HAVE user', () => {
      expect(comp.user.first_name).toBe('John',
        'should have user after service promise resolves');
    });

    it('should DISPLAY user', () => {
      // Find and examine the displayed user
      // Look for them in the DOM by css class
      const de = fixture.debugElement.query(By.css('h1'));
      el = de.nativeElement;
      expect(el.textContent).toContain(comp.user.first_name);
    });
  });


});


