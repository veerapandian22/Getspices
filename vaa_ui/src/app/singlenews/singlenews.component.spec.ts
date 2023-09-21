import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SinglenewsComponent } from './singlenews.component';

describe('SinglenewsComponent', () => {
  let component: SinglenewsComponent;
  let fixture: ComponentFixture<SinglenewsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SinglenewsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SinglenewsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
