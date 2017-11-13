import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkspaceEditionComponent } from './workspace-edition.component';

describe('WorkspaceEditionComponent', () => {
  let component: WorkspaceEditionComponent;
  let fixture: ComponentFixture<WorkspaceEditionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkspaceEditionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkspaceEditionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
