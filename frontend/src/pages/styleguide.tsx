import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const StyleGuidePage: React.FC = () => {
    return (
        <>
            <Navbar />
            <div className="global min-width-1024px">
                {/* Color Palette */}
                <div className="section">
                    <div className="grid grid-cols-2 gap-4">
                        <div className="container">
                            <h1 className="text-8xl font-bold p-0">
                                Visualise your <span className="text-linear-primary-accent">Colours</span> and style on a mock up
                            </h1>
                            <div className="container mt-8">
                                <div className="container flex justify-between">
                                    {/* Primary */}
                                    <div className="bg-primary rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Primary
                                    </div>

                                    {/* Secondary */}
                                    <div className="bg-secondary rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Secondary
                                    </div>

                                    {/* Accent */}
                                    <div className="bg-accent rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Accent
                                    </div>

                                    {/* Neutral */}
                                    <div className="bg-neutral rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Neutral
                                    </div>
                                </div>
                                <div className="container flex justify-between mt-24">
                                    {/* Info */}
                                    <div className="bg-info rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Info
                                    </div>

                                    {/* Success */}
                                    <div className="bg-success rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Success
                                    </div>

                                    {/* Warning */}
                                    <div className="bg-warning rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Warning
                                    </div>

                                    {/* Error */}
                                    <div className="bg-error rounded flex items-center justify-center mr-2 mb-2 text-text" style={{ width: '80px', height: '80px' }}>
                                        Error
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="container">
                            <div className="relative bg-background" style={{ width: '652px', height: '644px' }}>
                                {/* Box 1 */}
                                <div className="absolute bg-neutral rounded" style={{ width: '163px', height: '60px', top: '0px', left: '0px' }}></div>

                                {/* Box 2 */}
                                <div className="absolute bg-secondary rounded" style={{ width: '193px', height: '60px', top: '0px', left: '424px' }}></div>

                                {/* Box 3 */}
                                <div className="absolute bg-primary rounded" style={{ width: '335px', height: '324px', top: '68px', left: '80px' }}></div>

                                {/* Box 4 */}
                                <div className="absolute bg-secondary rounded" style={{ width: '193px', height: '175px', top: '68px', left: '424px' }}></div>

                                {/* Box 5 */}
                                <div className="absolute bg-neutral rounded" style={{ width: '70px', height: '259px', top: '234px', left: '1px' }}></div>

                                {/* Box 6 */}
                                <div className="absolute bg-text rounded" style={{ width: '166px', height: '169px', top: '401px', left: '80px' }}></div>

                                {/* Box 7 */}
                                <div className="absolute bg-neutral rounded" style={{ width: '160px', height: '80px', top: '400px', left: '255px' }}></div>

                                {/* Box 8 */}
                                <div className="absolute bg-primary rounded opacity-20" style={{ width: '193px', height: '79px', top: '401px', left: '424px' }}></div>

                                {/* Box 9 */}
                                <div className="absolute bg-secondary rounded" style={{ width: '70px', height: '142px', top: '502px', left: '1px' }}></div>

                                {/* Box 10 */}
                                <div className="absolute bg-neutral rounded" style={{ width: '160px', height: '80px', top: '490px', left: '255px' }}></div>

                                {/* Box 11 */}
                                <div className="absolute bg-accent rounded" style={{ width: '193px', height: '129px', top: '490px', left: '424px' }}></div>

                                {/* Box 12 */}
                                <div className="absolute bg-text rounded" style={{ width: '160px', height: '40px', top: '579px', left: '255px' }}></div>
                            </div>
                            <p className="text-xs italic">
                                Credit to https://www.realtimecolors.com/ for visualisation technique
                            </p>
                        </div>
                    </div>
                </div>

                {/* Typography */}
                <div className="section">
                    <div className="container inline-flex">
                        <h2 className="center text-4xl text-center font-bold text-linear-primary-accent">Typography</h2>
                    </div>
                    <div className="min-w-full prose grid grid-cols-3 gap-4">
                        <div className="container center">
                            <h2>Heading Two</h2>
                            <h3>Heading Three</h3>
                            <h4>Heading Four</h4>
                        </div>
                        <div className="container center">
                            <p className="font-bold">Body Bold</p>
                            <p className="font-semibold">Body Semi-Bold</p>
                            <p className="font-normal">Body Normal</p>
                            <p className="font-light">Body Light</p>
                            <p className="font-thin">Body Thin</p>
                        </div>
                        <div className="container center">
                            <p className="italic">Italic</p>
                            <a href="#">Example of a link</a>
                            <blockquote>
                                <p>"Lorem ipsum blockquote"</p>
                            </blockquote>
                            <ul>
                                <li>List item 1</li>
                                <li>List item 2</li>
                                <li>List item 3</li>
                            </ul>
                        </div>
                    </div>
                </div>

                {/* Buttons */}
                <div className="section prose">
                    <div className="container inline-flex">
                        <h2 className="center text-4xl text-center font-bold text-linear-primary-accent">Buttons</h2>
                    </div>
                    <div className="px-16 grid grid-cols-3 gap-4">
                        <div className="container">
                            <h3>Button</h3>
                            <button className="btn">Button</button>
                        </div>
                        <div className="container">
                            <h3>Buttons with brand colours</h3>
                            <button className="btn">Button</button>
                            <button className="btn btn-neutral">Neutral</button>
                            <button className="btn btn-primary">Primary</button>
                            <button className="btn btn-secondary">Secondary</button>
                            <button className="btn btn-accent">Accent</button>
                            <button className="btn btn-ghost">Ghost</button>
                            <button className="btn btn-link">Link</button>
                        </div>
                        <div className="container">
                            <h3>Active buttons</h3>
                            <button className="btn btn-active">Default</button>
                            <button className="btn btn-active btn-neutral">Neutral</button>
                            <button className="btn btn-active btn-primary">Primary</button>
                            <button className="btn btn-active btn-secondary">Secondary</button>
                            <button className="btn btn-active btn-accent">Accent</button>
                            <button className="btn btn-active btn-ghost">Ghost</button>
                            <button className="btn btn-active btn-link">Link</button>
                        </div>
                        <div className="container">
                            <h3>Buttons with state colours</h3>
                            <button className="btn btn-info">Info</button>
                            <button className="btn btn-success">Success</button>
                            <button className="btn btn-warning">Warning</button>
                            <button className="btn btn-error">Error</button>
                        </div>
                        <div className="container">
                            <h3>Outline buttons</h3>
                            <button className="btn btn-outline">Default</button>
                            <button className="btn btn-outline btn-primary">Primary</button>
                            <button className="btn btn-outline btn-secondary">Secondary</button>
                            <button className="btn btn-outline btn-accent">Accent</button>
                        </div>
                        <div className="container">
                            <h3>Button sizes</h3>
                            <button className="btn btn-lg">Large</button>
                            <button className="btn">Normal</button>
                            <button className="btn btn-sm">Small</button>
                            <button className="btn btn-xs">Tiny</button>
                        </div>
                        <div className="container">
                            <h3>Responsive button</h3>
                            <p className="text-xs font-thin">This button will have different sizes on different browser viewpoints</p>
                            <button className="btn btn-xs sm:btn-sm md:btn-md lg:btn-lg">Responsive</button>
                        </div>
                        <div className="container">
                            <h3>Disabled buttons</h3>
                            <button className="btn" disabled>Disabled using attribute</button>
                            <button className="btn btn-disabled" tabIndex={-1} role="button" aria-disabled="true">Disabled using class name</button>
                        </div>
                        <div className="container">
                            <h3>Button with loading spinner</h3>
                            <button className="btn btn-square">
                                <span className="loading loading-spinner"></span>
                            </button>
                        </div>
                    </div>
                </div>

                {/* Forms Section */}
                <div className="section">
                    <div className="container prose">
                        <h2 className="text-4xl text-center font-bold text-linear-primary-accent">Forms</h2>
                        <form className="space-y-4">
                            {/* Text Input */}
                            <div className="form-control">
                                <label className="input input-primary flex items-center gap-2">
                                    <input type="text" className="grow" placeholder="Search" />
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4 opacity-70">
                                        <path fillRule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clipRule="evenodd" />
                                    </svg>
                                </label>
                            </div>
                            <div className="form-control">
                                <label className="input input-bordered input-lg input-secondary flex items-center gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4 opacity-70">
                                        <path d="M2.5 3A1.5 1.5 0 0 0 1 4.5v.793c.026.009.051.02.076.032L7.674 8.51c.206.1.446.1.652 0l6.598-3.185A.755.755 0 0 1 15 5.293V4.5A1.5 1.5 0 0 0 13.5 3h-11Z" />
                                        <path d="M15 6.954 8.978 9.86a2.25 2.25 0 0 1-1.956 0L1 6.954V11.5A1.5 1.5 0 0 0 2.5 13h11a1.5 1.5 0 0 0 1.5-1.5V6.954Z" />
                                    </svg>
                                    <input type="text" className="grow" placeholder="Email" />
                                </label>
                            </div>
                            <div className="form-control">
                                <label className="input input-bordered input-sm input-accent flex items-center gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4 opacity-70">
                                        <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
                                    </svg>
                                    <input type="text" className="grow" placeholder="Username" />
                                </label>
                            </div>
                            <div className="form-control">
                                <label className="input input-ghost input-xs flex items-center gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="w-4 h-4 opacity-70">
                                        <path fillRule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clipRule="evenodd" />
                                    </svg>
                                    <input type="password" className="grow" value="password" readOnly />
                                </label>
                            </div>

                            {/* Checkbox */}
                            <div className="form-control">
                                <label className="cursor-pointer label">
                                    <span className="label-text">Remember me</span>
                                    <input type="checkbox" defaultChecked className="checkbox checkbox-secondary" />
                                </label>
                            </div>

                            {/* Radio Button */}
                            <div className="form-control">
                                <label className="label cursor-pointer">
                                    <span className="label-text">Male</span>
                                    <input type="radio" name="radio-10" className="radio radio-accent checked:bg-red-500" defaultChecked />
                                </label>
                                <label className="label cursor-pointer">
                                    <span className="label-text">Female</span>
                                    <input type="radio" name="radio-10" className="radio radio-accent checked:bg-blue-500" />
                                </label>
                            </div>

                            {/* Select Dropdown */}
                            <div className="form-control">
                                <label className="label">
                                    <span className="label-text">Select an option</span>
                                </label>
                                <select className="select select-bordered" defaultValue="">
                                    <option value="" disabled>Choose one</option>
                                    <option value="option1">Option 1</option>
                                    <option value="option2">Option 2</option>
                                    <option value="option3">Option 3</option>
                                </select>
                            </div>

                            {/* Textarea */}
                            <div className="form-control">
                                <label className="label">
                                    <span className="label-text">Message</span>
                                </label>
                                <textarea className="textarea textarea-bordered" placeholder="Your message"></textarea>
                            </div>

                            {/* File Input */}
                            <div className="form-control">
                                <label className="label">
                                    <span className="label-text">File Input</span>
                                </label>
                                <input type="file" className="file-input file-input-bordered w-full max-w-xs" />
                            </div>

                            {/* Range slider */}
                            <div className="form-control">
                                <label className="label">
                                    <span className="label-text">Range Slider</span>
                                </label>
                                <input type="range" min="0" max="100" defaultValue="40" className="range range-accent" />
                            </div>

                            {/* Toggle */}
                            <div className="form-control">
                                <label className="label">
                                    <span className="label-text">Toggle</span>
                                </label>
                                <div className="flex flex-col">
                                    <div className="form-control w-52">
                                        <label className="cursor-pointer label">
                                            <span className="label-text">Primary</span>
                                            <input type="checkbox" className="toggle toggle-primary" defaultChecked />
                                        </label>
                                    </div>
                                    <div className="form-control w-52">
                                        <label className="cursor-pointer label">
                                            <span className="label-text">Secondary</span>
                                            <input type="checkbox" className="toggle toggle-secondary" defaultChecked />
                                        </label>
                                    </div>
                                    <div className="form-control w-52">
                                        <label className="cursor-pointer label">
                                            <span className="label-text">Accent</span>
                                            <input type="checkbox" className="toggle toggle-accent" defaultChecked />
                                        </label>
                                    </div>
                                </div>
                            </div>

                            {/* Submit Button */}
                            <div className="form-control mt-6">
                                <button className="btn btn-primary">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>

            <Footer />
        </>
    );
};

export default StyleGuidePage;